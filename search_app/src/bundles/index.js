import { composeBundles, createCacheBundle } from 'redux-bundler'
import { bundles as sorghumBundles } from 'sorghum-search'
import { bundles as grameneBundles } from 'gramene-search'
import UIbundle from './searchUI'
import cache from "../utils/cache"

const URLs = {
  name: 'URLs',
  getReducer: () => {
    const initialState = {
      ensemblSite: '//ensembl.gramene.org',
      grameneData: '//data.gramene.org'
    };
    return (state = initialState, {type, payload}) => {
      return state;
    }
  },
  selectEnsemblURL: state => state.URLs.ensemblSite,
  selectGrameneAPI: state => state.URLs.grameneData
};

const bundle = composeBundles(
  ...sorghumBundles,
  ...grameneBundles,
  UIbundle,
  URLs,
  createCacheBundle(cache.set)
);


export default bundle;