import React, { Component } from "react";
import { render } from "react-dom";
//instead of import ReactDOM from "react-dom" then do ReactDom.render(_,_), we import {render} directly
//but usually we just do this in index.js instead of like this which is creating a component App.js and import it to index.js
import HomePage from "./HomePage";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";

// functional based components
export default function App(props) {

    return (<div>
        <HomePage />
        <RoomJoinPage />
        <CreateRoomPage />
    </div>)
}

// class based components
// export default class App extends Component {
//     constructor(props) {
//         super(props)
//     }

//     render() {
//         return (<div><HomePage /></div>)
//     }
// }

// const appDiv = document.getElementById("app");
// render(<App />, appDiv) //render App component inside app div