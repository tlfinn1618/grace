import React, { Component } from "react";
import { useLocation } from "react-router-dom";

import NavigationComponent from "../navigation/navigation";
import GIDLogo from "./logo";

export default class Header extends Component {
  render() {
    return (
      <div className="header-container">
        <div className="header-center">
          <div className="header-logo">
            <GIDLogo />
          </div>
          <div className="header-text">
            <div className="header-heading">Grace In The Desert</div>
            <div className="header-mission">
              Where no one misses the grace of God
            </div>
            <div className="header-subheading">Adventist Church</div>
          </div>
        </div>
        <NavigationComponent />
      </div>
    );
  }
}
