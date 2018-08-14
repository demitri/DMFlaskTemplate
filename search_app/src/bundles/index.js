import { composeBundles, createCacheBundle } from 'redux-bundler'
import sorghum from 'sorghum-search'
import gramene from 'gramene-search'
import UIbundle from './searchUI'
import cache from "../utils/cache"

const sorghumBundles = sorghum.bundles;
const grameneBundles = gramene.bundles;

const bundle = composeBundles(
  ...sorghumBundles,
  ...grameneBundles,
  UIbundle,
  createCacheBundle(cache.set)
);


export default bundle;