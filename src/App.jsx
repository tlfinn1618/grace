import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Header from "./components/header/header";
import Giving from "./components/pages/giving";
import About from "./components/pages/about";
import Home from "./components/pages/home";
import Ministries from "./components/pages/ministries";
import Prayers from "./components/pages/prayers";
import Worship from "./components/pages/worship";
import Auth from "./components/pages/auth";
import "./styles/main.scss";

function App() {
  return (
    <div className="container">
      <Router>
        <div>
          <Header />
          {/* <NavigationComponent /> */}
          <Routes>
            <Route
              path="/"
              exact
              element={<Home />}
            />
            <Route
              path="/about"
              element={<About />}
            />
            <Route
              path="/worship"
              element={<Worship />}
            />
            <Route
              path="/giving"
              element={<Giving />}
            />
            <Route
              path="/prayers"
              element={<Prayers />}
            />
            <Route
              path="/ministries"
              element={<Ministries />}
            />

            <Route
              path="auth"
              element={<Auth />}
            />

            <Route
              path="*"
              element={
                <div className="error-route">
                  <h1>Oops!</h1>
                  <p>That page you requested does not exist.</p>
                </div>
              }
            />
          </Routes>
        </div>
      </Router>
    </div>
  );
}

export default App;
