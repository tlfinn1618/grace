import React from "react";
import styled from "styled-components";

const WorshipCard = styled.div`
  background-color: ghostwhite;
  border: 1px solid lightgray;
  border-radius: 5px;
  padding: 10px;
`;

const Title = styled.div`
  color: black;
  font-size: 1.25em;
  font-family: "Futura";
  font-weight: 600;
`;
const Subtitle = styled.div`
  color: black;
  font-size: 1.1em;
  font-family: "Dakota";
  font-weight: 600;
`;
const Content = styled.div`
  color: black;
  font-family: "Futura";
  font-weight: 300;
`;

const Card = (props) => (
  <WorshipCard>
    <Title>Worship times</Title>
    <Subtitle>Sabbath School</Subtitle>
    <Content>Teaching begins at 9:45am</Content>
    <hr />
    <Subtitle>Call to Worship</Subtitle>
    <Content>Service begins at 10:50am</Content>
  </WorshipCard>
);

export default Card;
