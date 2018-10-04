import { composeBundles, createCacheBundle } from 'redux-bundler'
import { bundles as sorghumBundles } from 'sorghum-search'
import { bundles as grameneBundles } from 'gramene-search'
import UIbundle from './searchUI'
import cache from "../utils/cache"

const bundle = composeBundles(
  ...sorghumBundles,
  ...grameneBundles,
  UIbundle,
  createCacheBundle(cache.set)
);


export default bundle;