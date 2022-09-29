import React, { Component } from "react";
import GracePointLogo from "../images/graceLogo.svg";

export default class Header extends Component {
  render() {
    return (
      <div className="header-container">
        <div className="header-center">
          <img
            src={GracePointLogo}
            className="App-logo"
            alt="logo"
          />
          <div className="header-heading">Grace In The Desert</div>
          <div className="header-mission">
            Where no one misses the grace of God
          </div>
          <div className="header-subheading">Seventh Day Adventist Church</div>
        </div>
      </div>
    );
  }
}
