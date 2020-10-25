import Layout from '../components/layout'
function WeatherData({data}) {

    return(
            <Layout>
               <h1><u>{data.name}</u></h1>
               <h3>Weather conditions: {data.weather[0].main}</h3>
               <h3>Average Temperature: {data.main.temp} K</h3>
            </Layout>
    );
}

export async function getServerSideProps({query}) {

    const res = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${query.city}&appid=${yourAPIkey}`)
    const data = await res.json()
  
    return { props: { data } }
  }

export default WeatherData;