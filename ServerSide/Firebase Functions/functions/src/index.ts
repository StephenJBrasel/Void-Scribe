import * as functions from 'firebase-functions';

// Start writing Firebase Functions
// https://firebase.google.com/docs/functions/typescript

export const getTimestamp = functions.https.onRequest((request, response) => 
{
  const admin = require('firebase-admin');
  response.send(admin.firestore.FieldValue.serverTimestamp());
});

exports.timestampRequests = functions.firestore
    .document('Algorithm_Requests/{req_id}')
    .onCreate((event, context) => {

      const admin = require('firebase-admin');
      return event.ref.set({timestamp: admin.firestore.FieldValue.serverTimestamp()}, {merge: true})

    });

exports.tagRequestsForProcessing = functions.firestore
    .document('Algorithm_Requests/{req_id}')
    .onCreate((event, context) => {
      return event.ref.update({"Processed":false})
    });
