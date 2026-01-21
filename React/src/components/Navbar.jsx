import React from "react";
import "./Navbar.css";

export const Navbar = () => {
  return (
    <>
      <header>
      <nav class="flex">
      
        <div class="logo">
          <img src="gemun.png" alt="" />
        </div>

        <ul class="nav-links flex">
          <li><a href="#hero-section">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#skills">Skills</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </header>
    </>
  );
};
