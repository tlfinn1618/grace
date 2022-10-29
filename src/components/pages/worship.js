import React from "react";
import ReactPlayer from "react-player/youtube";
import Card from "../cards/card";

export default function Worship() {
  return (
    <div className="worship-container">
      <div className="worship-times-container">
        <Card title="Worship Times" />
        <div className="worship-location-card">
          <h3>Find us</h3>
          <div className="map">this is a map</div>
        </div>
      </div>
      <div className="worship-video-container">
        <div className="video-title">
          <h1>This is a Video</h1>
        </div>
        <div className="video-container">
          <ReactPlayer
            url="https://www.youtube.com/embed/99BElbgGVrk"
            controls={true}
          />
        </div>
      </div>
    </div>
  );
}
