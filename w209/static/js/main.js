/* global d3, scrollama */

const width = 400,
    height = 400;
    side = 30
const students = d3.range(20)
    .map(() => ({ x: Math.random() * width,
                  y: Math.random() * height }))

const images = d3.select("svg")
  .append("g")
  .selectAll('image')
  .data(students)
  .join('image')
  .attr('href', d => d.img)
  .attr("x", d => width / 2 - 15)
  .attr('y', d => height / 2 - 15)
  .attr('width', side)
  .attr('height', side)
  .attr('preserveAspectRatio', "xMidYMin slice");
function moveLeft() {
 images
    .transition()
    .duration(750)
    .attr("x", 20)
}

function moveX() {
 images
    .transition()
    .duration(750)
    .attr("x", (d) => Math.random() * (width - margin.left - margin.right - side / 2))
}

function moveY() {
images
    .transition()
    .duration(750)
    .attr("y", (d) => Math.random() * (height - margin.top - margin.bottom - side / 2))
}

//window.addEventListener("scroll", function (e) {
//    console.log(window.scrollY)
//})

const callbacks = [
    moveLeft,
    moveX,
    moveY,
    moveLeft,
    moveX,
    moveY,
    moveLeft,
    moveX,
    moveY,
    moveLeft,
    moveX
]

const steps = d3.selectAll(".step")

// instantiate the scrollama
const scroller = scrollama();

// setup the instance, pass callback functions
scroller
  .setup({
    step: ".step",
  })
  .onStepEnter((response) => {
    // { element, index, direction }
    callbacks[response.index]()

    steps.style("opacity", 0.1)
    d3.select(response.element).style("opacity", 1.0)

    console.log("enter", response)
  })
  .onStepExit((response) => {
    // { element, index, direction }
    console.log("exit", response)
  });

// setup resize event
window.addEventListener("resize", scroller.resize);
