import React from 'react'
import { render } from 'react-dom'
import getStore from './bundles'
import cache from './utils/cache'
import Summary from './components/summary'
import Results from './components/results'
import SearchBox from './components/searchbox'
import SearchBar from './components/searchbar'
import GeneSearchUI from './components/gramene-search'

cache.getAll().then(initialData => {
  if (initialData) {
    if (initialData.hasOwnProperty('searchUI')) initialData.searchUI.suggestions_query="";
    console.log('starting with locally cached data:', initialData)
  }
  const store = getStore(initialData);
  let element = document.getElementById('search-summary');
  element && render(Summary(store), element);

  element = document.getElementById('search-results');
  element && render(Results(store), element);

  element = document.getElementById('search-box');
  element && render(SearchBox(store), element);

  element = document.getElementById('sorghumbase-searchbar');
  element && render(SearchBar(store), element);

  element = document.getElementById('gene-search-ui');
  element && render(GeneSearchUI(store), element);
})
