import React from 'react'
import { render } from 'react-dom'
import getStore from './bundles'
import cache from './utils/cache'
import Summary from './components/summary'
import Results from './components/results'
import SearchBox from './components/searchbox'
import SearchBar from './components/searchbar'
import GeneSearchUI from './components/gramene-search'
import Feedback from './components/Feedback'
import MDView from "gramene-mdview";

const Notes = props => (
  <MDView
    org='warelab'
    repo='release-notes'
    path='sorghum'
    heading='Releases'
  />
)

cache.getAll().then(initialData => {
  if (initialData) {
    if (initialData.searchUI) initialData.searchUI.suggestions_query="";
    console.log('starting with locally cached data:', initialData)
  }
  const store = getStore(initialData);
  console.log('got store');
  let element = document.getElementById('search-summary');
  element && render(Summary(store), element) && console.log('rendered search-summary');

  element = document.getElementById('search-results');
  element && render(Results(store), element) && console.log('rendered search-results');

  element = document.getElementById('search-box');
  element && render(SearchBox(store), element) && console.log('rendered search-box');

  element = document.getElementById('sorghumbase-searchbar');
  element && render(SearchBar(store), element) && console.log('rendered sorghumbase-searchbar');

  element = document.getElementById('gene-search-ui');
  element && render(GeneSearchUI(store), element) && console.log('rendered gene-search-ui');

  element = document.getElementById('sorghumbase-feedback');
  element && render(Feedback(), element) && console.log('rendered sorghumbase-feedback')

  element = document.getElementById('sorghumbase-relnotes');
  element && render(Notes(), element) && console.log('rendered sorghumbase-relnotes')
})
