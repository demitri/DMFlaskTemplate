import { h } from 'preact'
import { Provider } from 'redux-bundler-preact'
import { resultList as Sorghum } from 'sorghum-search'
import { resultList as Gramene } from 'gramene-search'

export default (store) => (
  <Provider store={store}>
    <div>
      <Sorghum />
      <Gramene />
    </div>
  </Provider>
)
