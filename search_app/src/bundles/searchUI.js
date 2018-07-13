import qs from 'querystringify'

const isString = obj =>
  Object.prototype.toString.call(obj) === '[object String]'
const ensureString = input =>
  isString(input) ? input : qs.stringify(input)

const UIbundle = {
  name: 'searchUI',
  getReducer: () => {
    const initialState = {
      sorghumbase: true,
      Posts: true,
      Events: true,
      Jobs: true,
      People: true,
      Links: true,
      Papers: true,
      updates: 1,
      Gramene: true,
      Genes: true,
      Domains: false,
      Pathways: false,
      Species: false,
      rows: {
        Posts: 2,
        Events: 2,
        Jobs: 2,
        People: 2,
        Links: 2,
        Papers: 2,
        Genes: 20
      }
    };
    return (state = initialState, {type, payload}) => {
      if (type === 'CATEGORY_TOGGLED') {
        let update = {
          updates: state.updates + 1
        };
        update[payload] = !state[payload];
        return Object.assign(state, update)
      }
      if (type === 'CATEGORY_QUANTITY_CHANGED') {
        let update = {
          updates: state.updates + 1,
          rows: {}
        };
        update.rows[payload.cat] = state.rows[payload.cat] + payload.delta;
        return Object.assign(state, update)
      }
      return state
    }
  },
  doToggleCategory: cat => ({dispatch}) => {
    dispatch({type: 'CATEGORY_TOGGLED', payload: cat})
  },
  persistActions: ['CATEGORY_TOGGLED'],
  doChangeQuantity: (cat, delta) => ({dispatch}) => {
    dispatch({type: 'CATEGORY_QUANTITY_CHANGED', payload: {cat:cat, delta:delta}});
    if (cat === 'Genes') dispatch({type: 'GRAMENE_GENES_CLEARED'});
    if (cat === 'Posts') dispatch({type: 'SORGHUM_POSTS_CLEARED'});
    if (cat === 'Links') dispatch({type: 'SORGHUM_LINKS_CLEARED'});
    if (cat === 'Events') dispatch({type: 'SORGHUM_EVENTS_CLEARED'});
    if (cat === 'Jobs') dispatch({type: 'SORGHUM_JOBS_CLEARED'});
    if (cat === 'People') dispatch({type: 'SORGHUM_PEOPLE_CLEARED'});
    if (cat === 'Papers') dispatch({type: 'SORGHUM_PAPERS_CLEARED'});
  },
  doUpdateTheQueries: query => ({dispatch, getState}) => {
    const url = new URL(getState().url.url);
    url.search = ensureString(query);
    dispatch({
      type: 'BATCH_ACTIONS', actions: [
        {type: 'SORGHUM_POSTS_CLEARED'},
        {type: 'SORGHUM_LINKS_CLEARED'},
        {type: 'SORGHUM_JOBS_CLEARED'},
        {type: 'SORGHUM_EVENTS_CLEARED'},
        {type: 'SORGHUM_PEOPLE_CLEARED'},
        {type: 'SORGHUM_PAPERS_CLEARED'},
        {type: 'GRAMENE_GENES_CLEARED'},
        {type: 'GRAMENE_TAXONOMY_CLEARED'},
        {type: 'GRAMENE_DOMAINS_CLEARED'},
        {type: 'GRAMENE_PATHWAYS_CLEARED'},
        {type: 'URL_UPDATED', payload: {url: url.href, replace: false}}
      ]
    });
  },
  selectSearchUI: state => state.searchUI,
  selectSearchUpdated: state => state.searchUI.updates,
  selectRows: state=> state.searchUI.rows
};

export default UIbundle;