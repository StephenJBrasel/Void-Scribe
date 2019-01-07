import * as functions from 'firebase-functions';
import * as admin from 'firebase-admin'

// Start writing Firebase Functions
// https://firebase.google.com/docs/functions/typescript

admin.initializeApp(functions.config().firebase)
  

export const getTimestamp = functions.https.onRequest((request, response) => 
{

  response.send(admin.firestore.FieldValue.serverTimestamp());
});

export const voidScribeRequest = functions.https.onRequest((request, response) => 
{
  const collection = admin.firestore().collection('Algorithm_Requests')
  const doc = collection.doc()

  const data = request.body;


  return doc.set(data).then((result) => {
    response.status(200).json(doc.id)
  });
  
});

export const voidScribeRetreive = functions.https.onRequest((request, response) =>
{
  const data = request.body;
  const id = data["Doc_ID"];

  const collection = admin.firestore().collection('Completed_Requests')
  const query = collection.where("Req_Doc_ID", "==", String(id))

  return query.get().then((snapshot) => {
    if(snapshot.size === 1)
    {
      //response.send({data:snapshot.docs[0].data(), completed:true})
      response.status(200).json({data:snapshot.docs[0].data(), completed:true})
    }
    else
    {
      //response.send({completed:false});
      response.status(200).json({completed:false});
    }
  });
});

exports.timestampRequests = functions.firestore
    .document('Algorithm_Requests/{req_id}')
    .onCreate((event, context) => {

      return event.ref.set({timestamp: admin.firestore.FieldValue.serverTimestamp()}, {merge: true})

    });

exports.tagRequestsForProcessing = functions.firestore
    .document('Algorithm_Requests/{req_id}')
    .onCreate((event, context) => {
      return event.ref.update({"Processed":false})
    });
