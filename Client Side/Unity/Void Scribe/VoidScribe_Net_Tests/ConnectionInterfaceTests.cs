using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using VoidScribe.Connection;
using Google.Cloud.Firestore;
using System;
using System.Collections.Generic;
using VoidScribe.Connection;

namespace VoidScribe_Net_Tests
{
    [TestClass]
    public class ConnectionInterfaceTests
    {
        [TestMethod]
        public void TestConnection()
        {
            FirestoreDb db = ConnectionInterface.Connect();

            Assert.AreEqual("void-scribe", db.ProjectId);
        }
    }
}
