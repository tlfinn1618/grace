import React, { Component } from "react";

import Login from "../auth/login";

class Auth extends Component {
  render() {
    return (
      <div className="auth-wrapper">
        <Login />
      </div>
    );
  }
}

export default Auth;
