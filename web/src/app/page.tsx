"use client";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer"
import Image from "next/image";

export default function Home() {
  return (
    <>
    <Navbar></Navbar>
    <div className="container w-full mx-auto justify-center content-center max-w-none">
      {/* <h1 className="hero-title">A Pasionate Software Engineer Soon To Be Discovered</h1> */}
      <h1 className="hero-title">An Ordinary Man with an Incredible Dreams</h1>
      <div className="flex justify-center items-center gap-18 text-left basis-2xl">
        <div className="">
          <img className="w-full max-w-sm" src="/images/astronaut.png" alt="astro-moon" />
        </div >
      
        <div className="flex flex-col max-w-lg">
          <h2 className="text-3xl mb-7 uppercase">You have shared breakthroughs so far. Will the next one be you?</h2>
          <p className="mb-7">Receive ideas shared with millions of people each week directly to your inbox.</p>
          <div className="flex mb-7">
            <input className="inline-block border w-full placeholder:text-[0.8rem] placeholder:p-3 border-gray-600 rounded-3xl p-2" type="email" placeholder="Your Email Address"/>
            <button className="rounded-md border button-outline text-nowrap" type="submit">SIGN UP</button>
          </div>
          <p className="italic text-gray-600 text-[0.8rem]">Your information is protected and I never spam, ever. You can view my privacy policy here.</p>
        </div>
      </div>
    </div>
    <Footer></Footer>
    </>
  );
}
