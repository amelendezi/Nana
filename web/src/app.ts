import { createProjector, h } from "maquette";

// Maquette.js setup
const projector = createProjector();

const render = () => {
  return h("div", [
    h("h1", ["Nana!"]),
    h("p", ["This is a sample page for Nana, refrsh the page to see the changes."]),
  ]);
};

projector.append(document.body, render);
