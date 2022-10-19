import React, { Component } from "react";

class Login extends Component {
  render() {
    return (
      <div className="login-container">
        <div className="login-card">
          <div className="login-card-content">
            <div className="login-heading">LOGIN TO ACCESS YOUR DASHBOARD</div>
            <form className="login-form-wrapper">
              <div className="login-form-group">
                <input
                  type="email"
                  name="email"
                  placeholder="Enter your email"
                />
              </div>
              <div className="login-form-group">
                <input
                  type="password"
                  name="password"
                  placeholder="Enter your password"
                />
              </div>
              <div className="btn-wrapper">
                <button className="btn">Login</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    );
  }
}

export default Login;
