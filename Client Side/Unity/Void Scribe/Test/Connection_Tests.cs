using Microsoft.VisualStudio.TestTools.UnitTesting;
using VoidScribe.Connection;
using Google.Cloud.Firestore;
using System.Collections.Generic;
using System.Threading.Tasks;
using System;

namespace VoidScribe_NET_Tests
{
    [TestClass]
    public class Connection_Tests
    {
        [TestMethod]
        public void ConnectToProject()
        {
            FirestoreDb con =  ConnectionInterface.Connect();
            Assert.AreEqual(con.ProjectId, "void-scribe");
        }

        [TestMethod]
        public async void UploadDocument()
        {
            FirestoreDb con = ConnectionInterface.Connect();
            CollectionReference col_ref = con.Collection("Test_Collection");
            Dictionary<string, object> values = new Dictionary<string, object>();
            values.Add("Hello", "There");
            values.Add("General", "Kenobi");
            values.Add("Local_System_Time", System.DateTime.Now);
            string name = "UNIT_TEST_DOC_" + System.DateTime.Now.ToString();

            Task upload = ConnectionInterface.UploadDocument(col_ref, values, name);
            upload.Start();
            await upload;

            Assert.AreEqual(con.ProjectId, "void-scribe");
        }
    }
}
