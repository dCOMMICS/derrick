gsap.registerPlugin (ScrollTrigger);

const container = 
document.querySelector(".container");

const sections = 
gsap.utils.toArray (".container .panel"),

gsap.to(sections, {
    xPercent: -100 * (sections.length - 1),
    ease: "none",
    ScrollTrigger: {
        trigger: ".container",
        pin: true,
        scrub: 1,
        snap : 1 / (sections.length - 1),
        end:

        ()=> "+=" + container.offsetWidth,
    },
});