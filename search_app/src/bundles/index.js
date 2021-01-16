import { composeBundles, createCacheBundle } from 'redux-bundler'
import sorghumBundles from '../../sorghum-search/bundles'
import grameneBundles from '../../gramene-search/bundles'
import UIbundle from './searchUI'
import cache from "../utils/cache"
import initialState from '../../config.json';


const config = {
  name: 'config',
  getReducer: () => {
    return (state = initialState) => {
      return state;
    }
  },
  selectEnsemblURL: state => state.config.ensemblSite,
  selectGrameneAPI: state => state.config.grameneData,
  selectTargetTaxonId: state => state.config.targetTaxonId
};

const bundle = composeBundles(
  ...sorghumBundles,
  ...grameneBundles,
  UIbundle,
  config,
  createCacheBundle(cache.set)
);


export default bundle;