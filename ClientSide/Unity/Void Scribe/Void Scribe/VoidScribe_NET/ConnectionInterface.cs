using System;
using System.Collections.Generic;
using System.Net;
using Newtonsoft.Json;
using System.Threading;

namespace VoidScribe
{
    public class VoidScribeRequest
    {
        private string requestType;
        private Dictionary<string, object> requestArguments;

        private VoidScribeRequest(string requestType, Dictionary<string, object> requestArguments)
        {
            RequestType = requestType;
            RequestArguments = requestArguments;
        }

        public string RequestType { get => requestType; set => requestType = value; }
        public Dictionary<string, object> RequestArguments { get => requestArguments; set => requestArguments = value; }

        public static VoidScribeRequest NameRequest(string nameType, int amount)
        {
            Dictionary<string, object> arguments = new Dictionary<string, object>();

            arguments.Add("Amount", amount);
            arguments.Add("Name_Type", nameType);

            return new VoidScribeRequest("Name", arguments);
        }

        public static VoidScribeRequest SentenceRequest(string sentenceType, int amount)
        {
            Dictionary<string, object> arguments = new Dictionary<string, object>();

            arguments.Add("Amount", amount);
            arguments.Add("Sentence_Type", sentenceType);

            return new VoidScribeRequest("Sentence", arguments);
        }

        public Dictionary<string, object> ToJSON()
        {
            Dictionary<string, object> data = new Dictionary<string, object>();

            data.Add("Req_Type", RequestType);
            data.Add("Req_Arguments", RequestArguments);
            data.Add("Req_Source", "Unity");
            data.Add("User_ID", "Unity_ID");

            return data;
        }
    }

    public class VoidScribeResult
    {
        private Dictionary<string, object> data;
        private bool successful;
        string error;

        public VoidScribeResult(Dictionary<string, object> data, bool successful, string error)
        {
            Data = data;
            Successful = successful;
            Error = error;
        }

        public Dictionary<string, object> Data { get => data; set => data = value; }
        public bool Successful { get => successful; set => successful = value; }
        public string Error { get => error; set => error = value; }
    }

    public delegate void VoidScribeCallback(VoidScribeResult result);

    public static class VoidScribeConnection
    {
        private static string PUT_URL = @"https://us-central1-void-scribe.cloudfunctions.net/voidScribeRequest";
        private static string RETR_URL = @"https://us-central1-void-scribe.cloudfunctions.net/voidScribeRetreive";

        public static void Request(VoidScribeCallback completion_callback, VoidScribeRequest request_data)
        {
            string req_ID = JSON_POST(PUT_URL, request_data.ToJSON());

            Dictionary<string, object> req = new Dictionary<string, object>();
            req.Add("Doc_ID", req_ID);

            Dictionary<string, object> http_result = JSON_PUT(RETR_URL, req);

            while ((bool)http_result["completed"] != true)
            {
                http_result = JSON_PUT(RETR_URL, req);
                Thread.Sleep(500);
            }

            VoidScribeResult result = new VoidScribeResult(http_result, true, "None");
            completion_callback(result);
        }

        private static string JSON_POST(string URL, Dictionary<string, object> data)
        {
            using (var client = new WebClient())
            {
                var dataString = JsonConvert.SerializeObject(data);
                client.Headers.Add(HttpRequestHeader.ContentType, "application/json");
                return client.UploadString(new Uri(URL), "POST", dataString);
            }
        }

        private static Dictionary<string, object> JSON_PUT(string URL, Dictionary<string, object> data)
        {

            object retreived = null;
            using (var client = new WebClient())
            {
                var dataString = JsonConvert.SerializeObject(data);
                client.Headers.Add(HttpRequestHeader.ContentType, "application/json");
                string temp = client.UploadString(URL, "PUT", dataString);
                Newtonsoft.Json.Linq.JObject jObject = JsonConvert.DeserializeObject(temp) as Newtonsoft.Json.Linq.JObject;
                return jObject.ToObject<Dictionary<string, object>>();
            }


            //return new Dictionary<string, object>();
        }
    }

}
