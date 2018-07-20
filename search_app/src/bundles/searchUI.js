import qs from 'querystringify'
import {createSelector} from 'redux-bundler'

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
                Posts: 6,
                Events: 6,
                Jobs: 6,
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
                return Object.assign(state, update)
            }
            if (type === 'CATEGORY_QUANTITY_CHANGED') {
                let newState = Object.assign(state, {
                    updates: state.updates + 1
                });
                newState.rows[payload.cat] += payload.delta;
                return newState;
            }
            return state
        }
    },
    doToggleCategory: cat => ({dispatch}) => {
        dispatch({type: 'CATEGORY_TOGGLED', payload: cat})
    },
    persistActions: ['CATEGORY_TOGGLED', 'CATEGORY_QUANTITY_CHANGED'],
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
    selectRows: state => state.searchUI.rows
};

export default UIbundle;