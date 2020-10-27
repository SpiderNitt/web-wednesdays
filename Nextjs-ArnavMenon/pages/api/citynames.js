import cities from './cities.json'

export default (req, res) => {
  res.status(200).json(cities)
}
