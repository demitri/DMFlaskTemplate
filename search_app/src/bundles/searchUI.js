import qs from 'querystringify'

const isString = obj =>
    Object.prototype.toString.call(obj) === '[object String]'
const ensureString = input =>
    isString(input) ? input : qs.stringify(input)
const clearResults = [
  {type: 'SORGHUM_POSTS_CLEARED'},
  {type: 'SORGHUM_PROJECTS_CLEARED'},
  {type: 'SORGHUM_LINKS_CLEARED'},
  {type: 'SORGHUM_EVENTS_CLEARED'},
  {type: 'SORGHUM_PEOPLE_CLEARED'},
  {type: 'SORGHUM_PAPERS_CLEARED'},
  {type: 'GRAMENE_GENES_CLEARED'},
  {type: 'GRAMENE_TAXONOMY_CLEARED'},
  {type: 'GRAMENE_DOMAINS_CLEARED'},
  {type: 'GRAMENE_PATHWAYS_CLEARED'}
];
const clearSuggestions = [
  {type: 'SORGHUM_POSTS_SUGGESTIONS_CLEARED'},
  {type: 'SORGHUM_PROJECTS_SUGGESTIONS_CLEARED'},
  {type: 'SORGHUM_LINKS_SUGGESTIONS_CLEARED'},
  {type: 'SORGHUM_EVENTS_SUGGESTIONS_CLEARED'},
  {type: 'SORGHUM_PEOPLE_SUGGESTIONS_CLEARED'},
  {type: 'SORGHUM_PAPERS_SUGGESTIONS_CLEARED'},
  {type: 'GRAMENE_SUGGESTIONS_CLEARED'},
  {type: 'SUGGESTIONS_CLEARED'}
];
const UIbundle = {
  name: 'searchUI',
  getReducer: () => {
    const initialState = {
      suggestions_query: '',
      suggestions_tab: 'sorghumbase',
      sorghumbase: true,
      Posts: true,
      Projects: true,
      Events: true,
      People: true,
      Links: true,
      Papers: true,
      updates: 1,
      Gramene: false,
      Genes: true,
      Domains: false,
      Pathways: false,
      Species: false,
      rows: {
        Posts: 6,
        Projects: 6,
        Events: 6,
        People: 6,
        Links: 6,
        Papers: 6,
        Genes: 20
      }
    };
    return (state = initialState, {type, payload}) => {
      if (type === 'CATEGORY_TOGGLED') {
        let update = {
          updates: state.updates + 1
        };
        update[payload] = !state[payload];
        return Object.assign({}, state, update)
      }
      if (type === 'CATEGORY_QUANTITY_CHANGED') {
        let newState = Object.assign({}, state, {
          updates: state.updates + 1
        });
        newState.rows[payload.cat] += payload.delta;
        return newState;
      }
      if (type === 'SUGGESTIONS_QUERY_CHANGED') {
        return Object.assign({}, state, {
          suggestions_query: payload.query
        });
      }
      if (type === 'SUGGESTIONS_TAB_CHANGED') {
        return Object.assign({}, state, {
          suggestions_tab: payload.key
        });
      }
      if (type === 'SUGGESTIONS_CLEARED') {
        return Object.assign({}, state, {
          suggestions_query: ''
        });
      }
      return state
    }
  },
  doToggleCategory: cat => ({dispatch}) => {
    dispatch({type: 'CATEGORY_TOGGLED', payload: cat})
  },
  persistActions: ['CATEGORY_TOGGLED', 'CATEGORY_QUANTITY_CHANGED', 'SUGGESTIONS_TAB_CHANGED', 'SUGGESTIONS_CLEARED'],
  doChangeQuantity: (cat, delta) => ({dispatch, getState}) => {
    const state = getState();
    console.log('doChangeQuantity', state);
    dispatch({type: 'CATEGORY_QUANTITY_CHANGED', payload: {cat: cat, delta: delta}});

    function possiblyFetch(category, delta) {
      const bundleName = category === 'Genes' ? 'Gramene' : 'Sorghum';
      const data = state[bundleName.toLowerCase() + category].data;
      const rows = state.searchUI.rows[category] + delta;
      if (bundleName === 'Gramene') {
        if (data && rows > data.response.docs.length && data.response.docs.length < data.response.numFound) {
          dispatch({actionCreator: `doFetch${bundleName}${category}`})
        }
      }
      if (bundleName === 'Sorghum') {
        if (data && rows > data.docs.length && data.docs.length < data.numFound) {
          dispatch({actionCreator: `doFetch${bundleName}${category}`})
        }
      }
    }

    possiblyFetch(cat, delta);
  },
  doChangeSuggestionsQuery: query => ({dispatch, getState}) => {
    dispatch({
      type: 'BATCH_ACTIONS', actions: [
        ...clearSuggestions,
        {type: 'SUGGESTIONS_QUERY_CHANGED', payload: {query: query.trim()}}
      ]
    });
  },
  doClearSuggestions: () => ({dispatch, getState}) => {
    document.getElementById('sorghumbase-searchbar-parent').classList.remove('search-visible');
    dispatch({
      type: 'BATCH_ACTIONS', actions: clearSuggestions
    });
  },
  doUpdateTheQueries: query => ({dispatch, getState}) => {
    const url = new URL(getState().url.url);
    url.search = ensureString(query);
    dispatch({
      type: 'BATCH_ACTIONS', actions: [
        ...clearResults,
        {type: 'URL_UPDATED', payload: {url: url.href, replace: false}}
      ]
    });
  },
  doAcceptSorghumSuggestion: query => ({dispatch, getState}) => {
    const url = new URL(getState().url.url);
    url.search = ensureString(query);
    const updateLocation = (url.pathname !== '/search');
    url.pathname = '/search';
    dispatch({
      type: 'BATCH_ACTIONS', actions: [
        ...clearSuggestions,
        ...clearResults,
        {type: 'URL_UPDATED', payload: {url: url.href, replace: false}}
      ]
    });
    document.getElementById('sorghumbase-searchbar-parent').classList.remove('search-visible');
    if (updateLocation) {
      window.location = url
    }
  },
  doAcceptGrameneSuggestion: suggestion => ({dispatch, getState}) => {
    const url = new URL(getState().url.url);
    if (url.pathname !== '/genes' && url.pathname !== '/genes.html') {
      url.pathname = '/genes';
      url.search = `suggestion=${JSON.stringify(suggestion)}`;
      window.location = url;
    }
    else {
      document.getElementById('sorghumbase-searchbar-parent').classList.remove('search-visible');
      dispatch({
        type: 'BATCH_ACTIONS', actions: [
          ...clearSuggestions,
          {type: 'GRAMENE_SEARCH_CLEARED'},
          {type: 'GRAMENE_FILTER_ADDED', payload: suggestion}
        ]
      });
    }
  },
  doChangeSuggestionsTab: key => ({dispatch, getState}) => {
    const currentTab = getState().suggestions_tab;
    if (key !== currentTab) {
      dispatch({
        type: 'SUGGESTIONS_TAB_CHANGED', payload: {key: key}
      })
    }
  },
  selectSearchUI: state => state.searchUI,
  selectSearchUpdated: state => state.searchUI.updates,
  selectRows: state => state.searchUI.rows,
  selectSuggestionsQuery: state => state.searchUI.suggestions_query,
  selectSuggestionsTab: state => state.searchUI.suggestions_tab,
  selectPath: state => state.pathname,
  selectSorghumSuggestionsStatus: state => {
    let matches=0;
    let loading=0;
    if (state.sorghumPostsSuggestions.data) matches += state.sorghumPostsSuggestions.data.numFound;
    else loading++;
    if (state.sorghumProjectsSuggestions.data) matches += state.sorghumProjectsSuggestions.data.numFound;
    else loading++;
    if (state.sorghumLinksSuggestions.data) matches += state.sorghumLinksSuggestions.data.numFound;
    else loading++;
    if (state.sorghumPeopleSuggestions.data) matches += state.sorghumPeopleSuggestions.data.numFound;
    else loading++;
    if (state.sorghumEventsSuggestions.data) matches += state.sorghumEventsSuggestions.data.numFound;
    else loading++;
    if (state.sorghumPapersSuggestions.data) matches += state.sorghumPapersSuggestions.data.numFound;
    else loading++;
    return loading ? 'loading' : `${matches} match${matches !== 1 ? 'es' : ''}`;
  }
};

export default UIbundle;