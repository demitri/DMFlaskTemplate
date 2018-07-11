import { composeBundles, createCacheBundle } from 'redux-bundler'
import { bundles as sorghum } from 'sorghum-search'
import { bundles as gramene } from 'gramene-search'
import UIbundle from './searchUI'
import cache from '../utils/cache'

const bundle = composeBundles(
  ...sorghum,
  ...gramene,
  UIbundle,
  createCacheBundle(cache.set)
);


export default bundle;