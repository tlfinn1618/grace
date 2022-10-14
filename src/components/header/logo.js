import React, { Component } from "react";

import GracePointLogo from "../../images/header/graceLogo.svg";

class GIDLogo extends Component {
  render() {
    const size = {
      width: this.props.width ? this.props.width : 270,
      height: this.props.height ? this.props.height : 278
    };
    return (
      <div className="app-logo-wrapper">
        <img
          style={size}
          src={GracePointLogo}
          className="App-logo"
          alt="logo"
        />
      </div>
    );
  }
}

export default GIDLogo;
