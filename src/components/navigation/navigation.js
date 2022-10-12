import React, { Component } from "react";

export default class NavigationComponent extends Component {
  render() {
    return (
      <div className="navBar-wrapper">
        <div className="nav-btn">Home</div>
        <div>Worship</div>
        <div>About</div>
        <div>Events</div>
        <div>Giving</div>
        <div>Prayers</div>
        <div>Ministries</div>
      </div>
    );
  }
}
