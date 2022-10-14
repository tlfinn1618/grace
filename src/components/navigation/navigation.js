import React, { Component } from "react";
import { NavLink } from "react-router-dom";

export default class NavigationComponent extends Component {
  render() {
    return (
      <div className="navBar-wrapper">
        <NavLink
          to="/home"
          className="nav-btn"
        >
          Home
        </NavLink>
        <NavLink
          to="/worship"
          className="nav-btn"
        >
          Worship
        </NavLink>
        <NavLink
          to="/about"
          className="nav-btn"
        >
          About
        </NavLink>
        <NavLink
          to="/giving"
          className="nav-btn"
        >
          Giving
        </NavLink>
        <NavLink
          to="/prayers"
          className="nav-btn"
        >
          Prayers
        </NavLink>
        <NavLink
          to="/ministries"
          className="nav-btn"
        >
          Ministries
        </NavLink>
      </div>
    );
  }
}
