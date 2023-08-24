import React, { Component } from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import { 
        BrowserRouter as Router, 
        Switch, 
        Route, 
        Link, 
        Redirect,
        Routes, 
    } from "react-router-dom";


//<switch> is basically switch statement
export default function HomePage(props) {
    console.log("home")
    return (
        <div>this is home</div>
    // <Router>
    //     <Routes> 
    //         <Route exact path="/" element={<p>This is the homepage</p>} />
    //         <Route path="/join" element={RoomJoinPage} />
    //         <Route path="/create" element={CreateRoomPage} />
    //     </Routes>
    // </Router>
    );
}

// export default class HomePage extends Component {
//     constructor(props) {
//         super(props);
//     }
//     render() {
//         return (
//                 <Router>
//                     <Routes> 
//                         <Route exact path="/" element={<p>This is the homepage</p>} />
//                         <Route path="/join" element={RoomJoinPage} />
//                         <Route path="/create" element={CreateRoomPage} />
//                     </Routes>
//                 </Router>);
//     }
// }