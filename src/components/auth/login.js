import React, { Component } from "react";

import axios from "axios";

class Login extends Component {
  constructor(props) {
    super(props);

    this.state = {
      email: "",
      password: "",
      errorText: ""
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value,
      errorText: ""
    });
  }

  handleSubmit(event) {
    axios
      .post(
        "https://api.devcamp.space/sessions",
        {
          client: {
            email: this.state.email,
            password: this.state.password
          }
        },
        { withCredentials: true }
      )
      .then((response) => {
        if (response.data.status === "created") {
          console.log("you may pass...");
        } else {
          this.setState({
            errorText: "Wrong email or password"
          });
        }
      })
      .catch((error) => {
        this.setState({
          errorText: "An error occurred"
        });
      });
    event.preventDefault();
  }

  render() {
    return (
      <div className="login-container">
        <div className="login-card">
          <div className="login-card-content">
            <div className="login-heading">ACCESS YOUR DASHBOARD</div>

            <div>{this.state.errorText}</div>

            <form
              className="login-form-wrapper"
              onSubmit={this.handleSubmit}
            >
              <div className="login-form-group">
                <input
                  type="email"
                  name="email"
                  placeholder="Enter your email"
                  value={this.state.email}
                  onChange={this.handleChange}
                />
              </div>
              <div className="login-form-group">
                <input
                  type="password"
                  name="password"
                  placeholder="Enter your password"
                  value={this.state.password}
                  onChange={this.handleChange}
                />
              </div>
              <div className="btn-wrapper">
                <button
                  className="btn"
                  type="submit"
                >
                  Login
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    );
  }
}

export default Login;
