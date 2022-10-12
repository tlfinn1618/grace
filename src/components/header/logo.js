import React, { Component } from "react";

import GracePointLogo from "../../images/header/graceLogo.svg";

class GIDLogo extends Component {
  render() {
    return (
      <div className="app-logo-wrapper">
        <img
          src={GracePointLogo}
          className="App-logo"
          alt="logo"
        />
      </div>
    );
  }
}

export default GIDLogo;
