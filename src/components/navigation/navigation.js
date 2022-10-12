import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class NavigationComponent extends Component {
  render() {
    return (
      <div className="navBar-wrapper">
        <Link
          to="/home"
          className="nav-btn"
        >
          Home
        </Link>
        <Link
          to="/worship"
          className="nav-btn"
        >
          Worship
        </Link>
        <Link
          to="/about"
          className="nav-btn"
        >
          About
        </Link>
        <Link
          to="/events"
          className="nav-btn"
        >
          Events
        </Link>
        <Link
          to="/giving"
          className="nav-btn"
        >
          Giving
        </Link>
        <Link
          to="/prayers"
          className="nav-btn"
        >
          Prayers
        </Link>
        <Link
          to="/ministries"
          className="nav-btn"
        >
          Ministries
        </Link>
      </div>
    );
  }
}
