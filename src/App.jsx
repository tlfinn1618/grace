import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import NavigationComponent from "./components/navigation/navigation";
import Giving from "./components/pages/giving";
import About from "./components/pages/about";
import Home from "./components/pages/home";
import Ministries from "./components/pages/ministries";
import Prayers from "./components/pages/prayers";
import Worship from "./components/pages/worship";
import "./styles/main.scss";

function App() {
  return (
    <Router>
      <NavigationComponent />
      <Routes>
        <Route
          path="/home"
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
      </Routes>
    </Router>
  );
}

export default App;
