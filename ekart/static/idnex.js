
let tm =gsap.timeline()
tm.from("#header img, #header", {
    y:-50,
    // scale:1.3,
    duration:1
})
tm.from("#navbar li", {
    y:-50,
    stagger:0.5
})

tm.from("#hero h4, #hero h6", {
    x:-150,
    duration:1,
    // stagger:1
})
tm.from("#hero h1", {
    x:150,
    duration:1,
    stagger:1
})
tm.from("#hero h1 span", {
    x:-150,
    duration:1,
    stagger:1
})
tm.from("#hero button", {
    scale:1.5,
    duration:1,
    rotate:360
})
