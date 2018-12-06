import React from 'react';
import {FlatList, ScrollView, View, Text, TextInput, Button, } from 'react-native';
import firebase from 'react-native-firebase';
import Todo from './Todo'; // we'll create this next

export default class Todos extends React.Component {
  
    constructor() {
      super();
      this.ref = firebase.firestore().collection('TEST_COLLECTION');
      this.state = {
        textInput: '',
        amountInput: '',
        todos: [],
        loading: true,
              
      };
          
    }
    componentDidMount() {
      this.unsubscribe = this.ref.onSnapshot(this.onCollectionUpdate) 
    }
    componentWillUnmount() {
      this.unsubscribe();
    }

    updateTextInput(value) {
      //const { currentUser } = firebase.auth()
      this.setState({ textInput: value});
    }
    updateAmountInput(value) {
      //const { currentUser } = firebase.auth()
      this.setState({ amountInput: value});
    }
    addTodo() {
      const generateKey = (pre) => {
        return `${ pre }_${ new Date().getTime() }`;
      }
    
    
      const Req_list = 
      {
        Name_Type: this.state.textInput ,
        Amount:  Number.parseInt(this.state.amountInput),
            
      }
      this.ref.add({
        Req_Type: 'Name',
        Req_Arguments: Req_list,
        User_ID: firebase.auth().currentUser.uid,
        Request_Source: 'Mobile',
        Auth_Token: firebase.auth().currentUser.getIdToken(),
        Hash_Key: generateKey(firebase.auth().currentUser.uid),
        });
      this.setState({
        textInput: '',
        amountInput: '',
      });
    }
    onCollectionUpdate = (querySnapshot) => {
      const todos = [];
      querySnapshot.forEach((doc) => {
        const { Req_Type, User_ID } = doc.data();
        todos.push({
          key: doc.id,
          doc, // DocumentSnapshot
          Req_Type,
          User_ID ,
        });
      });
      this.setState({ 
        todos,
        loading: false,
     });
  }
    
    render() {
    if (this.state.loading) {
        return null; // or render a loading icon
    }
    return (
        <View>
          <ScrollView>
          <FlatList
                data={this.state.todos}
                renderItem={({ item }) => <Todo {...item} />}
              />
            <Text></Text>
            <Text>Create list of Names</Text>
          </ScrollView>
          <TextInput
            placeholder={'Add Nametype'}
            value={this.state.textInput}
            onChangeText={(text) => this.updateTextInput(text)}
          />
          <TextInput
            placeholder={'Add Amount'}
            value={this.state.amountInput}
            onChangeText={(text) => this.updateAmountInput(text)}
          />
          <Button
            title={'Generate Name'}
            disabled={!this.state.textInput.length}
            disabled={!this.state.amountInput.length}
            onPress={() => this.addTodo()}
          />
          
        </View>
      );
    }
}
