import { h } from 'preact'
import { Provider } from 'redux-bundler-preact'
import { resultSummary as Sorghum } from 'sorghum-search'
import { resultSummary as Gramene } from 'gramene-search'

export default (store) => (
  <Provider store={store}>
    <ul class="list-unstyled category">
      <Sorghum />
      <Gramene />
    </ul>
  </Provider>
)
