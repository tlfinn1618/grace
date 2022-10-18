import React, { Component } from "react";
import { NavLink } from "react-router-dom";

export default class NavigationComponent extends Component {
  render() {
    let activeStyle = {
      textDecoration: "none",
      color: "white",
      backgroundColor: "gray",
      padding: "5px 10px",
    };

    let navBtn = {
      textDecoration: "none",
      color: "black",
      padding: "5px 10px",
      transition: "500ms",
    };

    return (
      <div className="navBar-wrapper">
        <div className="navBar-left">
          <NavLink
            style={({ isActive }) => (isActive ? activeStyle : navBtn)}
            end
            to="/"
          >
            Home
          </NavLink>
          <NavLink
            style={({ isActive }) => (isActive ? activeStyle : navBtn)}
            end
            to="/worship"
          >
            Worship
          </NavLink>
          <NavLink
            style={({ isActive }) => (isActive ? activeStyle : navBtn)}
            end
            to="/about"
          >
            About
          </NavLink>
          <NavLink
            style={({ isActive }) => (isActive ? activeStyle : navBtn)}
            end
            to="/giving"
          >
            Giving
          </NavLink>
          <NavLink
            style={({ isActive }) => (isActive ? activeStyle : navBtn)}
            end
            to="/prayers"
          >
            Prayers
          </NavLink>
          <NavLink
            style={({ isActive }) => (isActive ? activeStyle : navBtn)}
            end
            to="/ministries"
          >
            Ministries
          </NavLink>
        </div>
        <div className="navbar-right">
          {/* Log in status - visible when logged in */}
        </div>
      </div>
    );
  }
}
