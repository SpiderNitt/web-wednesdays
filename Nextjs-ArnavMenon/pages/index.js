import fetch from 'isomorphic-unfetch';
import Link from "next/link";
import React from 'react'
import Layout from '../components/layout'

function Index ({data}) {
    return (
            <Layout>
                <h1>List of Cities</h1>
                {data.map((item, i) => (
                   <li key={i}>
                    <Link as={`/${item.city}`} href="/[city]">
                      <a> {item.city} </a>
                    </Link>
                    </li>
                   
               ))}
            </Layout>
    );
}

export async function getStaticProps(){
    const res = await fetch(`http://localhost:3000/api/citynames`);
    const data = await res.json();
    return { 
      props: { data }
    }
}

export default Index;