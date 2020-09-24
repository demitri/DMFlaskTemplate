import { composeBundles, createCacheBundle } from 'redux-bundler'
import { bundles as sorghumBundles } from 'sorghum-search'
import { bundles as grameneBundles } from 'gramene-search'
import UIbundle from './searchUI'
import cache from "../utils/cache"
const initialState = require('../../config.json');


const config = {
  name: 'config',
  getReducer: () => {
    return (state = initialState, {type, payload}) => {
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