import Link from 'next/link'
import { useState } from 'react'
import Image from 'next/image'
import RightArrowIcon from "@/components/RightIcon";

export default function Navbar() {


  return (
    <footer className="bg-black text-white">
        <div className="flex flex-column justify-between text-left">
            <div className='footer-about basis-1/2 pt-18 pr-10 pb-9 pl-90'>
                <Image width={99} height={27} src="/images/lerry-light.png" alt="lerry-logo" priority />
                <p className=''>Mark is the three-time #1 New York Times bestselling author of The Subtle Art of Not Giving a F*ck, as well as other titles. 
                    His books have sold around 20 million copies, been translated into more than 65 languages, and reached number one in more than a dozen countries.
                    In 2023, a feature film about his life and ideas was released worldwide by Universal Pictures.
                </p>
                <RightArrowIcon></RightArrowIcon>
                <button className='uppercase'> learn more about lerry</button>
                <div className="text-gray-400 text-[0.8rem]">© 2025 John Lerry Laungayan Co. LTD.</div>
            </div>
            <div className='footer-nav basis-1/2'>
                <div className='pt-14 px-0 pb-9'>
                    <div className='pr-90 pb-14'>
                        <div className='grid grid-cols-2 grid-rows-4 pl-28 uppercase leading-4'>
                            <a className='a-link-light' href="/home">home</a>
                            <a className='a-link-light' href="/blog">blog</a>
                            <a className='a-link-light' href="/projects">projects</a>
                            <a className='a-link-light' href="/resume">resume</a>
                            <a className='a-link-light' href="/sign-up">sign up</a>
                            <a className='a-link-light' href="/about">about lerry</a>
                            <a className='a-link-light' href="/contact">contact</a>
                            <a className='a-link-light' href="/sponsorships">sponsorships</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>
  )
}
