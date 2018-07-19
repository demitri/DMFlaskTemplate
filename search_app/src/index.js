import {render} from 'preact'
import getStore from './bundles'
import cache from './utils/cache'
import Summary from './components/summary'
import Results from './components/results'
import SearchBox from './components/searchbox'

cache.getAll().then(initialData => {
  if (initialData) {
    console.log('starting with locally cached data:', initialData)
  }
  const store = getStore();//initialData);
  render(Summary(store), document.getElementById('search-summary'));
  render(Results(store), document.getElementById('search-results'));
  render(SearchBox(store), document.getElementById('search-box'));
})
