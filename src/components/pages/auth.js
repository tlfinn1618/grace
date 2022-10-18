import React, { Component } from "react";

import Login from "../auth/login";

class Auth extends Component {
  render() {
    return (
      <div className="auth-wrapper">
        <div className="auth-wrapper-left">left</div>
        <div className="auth-wrapper-right">
          <Login />
        </div>
      </div>
    );
  }
}

export default Auth;
