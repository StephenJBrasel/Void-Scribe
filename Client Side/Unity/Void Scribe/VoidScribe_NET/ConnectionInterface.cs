using System;
using System.Collections.Generic;
using System.Net;

namespace VoidScribe
{
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
    }

    public static class VoidScribeConnection
    {
        public static void Request(VoidScribeCallback completion_callback, VoidScribeRequest request_data)
        {
            SendHTTPRequest(request_data);
        }

        private static void SendHTTPRequest(VoidScribeRequest request_data)
        {
            WebClient client = new System.Net.WebClient();
            client.Headers[HttpRequestHeader.ContentType] = "application/json";
            client.BaseAddress = "ENDPOINT URL";
            string response = client.DownloadString(string.Format("{0}?{1}", Url, parameters.UrlEncode()));
        }
    }

}
