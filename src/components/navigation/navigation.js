import React, { Component } from "react";
import { NavLink } from "react-router-dom";

export default class NavigationComponent extends Component {
  render() {
    let className = "nav-btn";

    return (
      <div className="navBar-wrapper">
        <div className="navBar-left">
          <NavLink
            className={className}
            end
            to="/"
          >
            Home
          </NavLink>
          <NavLink
            className={className}
            end
            to="/worship"
          >
            Worship
          </NavLink>
          <NavLink
            className={className}
            end
            to="/about"
          >
            About
          </NavLink>
          <NavLink
            className={className}
            end
            to="/giving"
          >
            Giving
          </NavLink>
          <NavLink
            className={className}
            end
            to="/prayers"
          >
            Prayers
          </NavLink>
          <NavLink
            className={className}
            end
            to="/ministries"
          >
            Ministries
          </NavLink>
          <NavLink
            className={className}
            end
            to="/dashboard"
          >
            Dashboard
          </NavLink>
        </div>
        <div className="navbar-right">
          {/* Log in status - visible when logged in */}
        </div>
      </div>
    );
  }
}
