import { h } from 'preact'
import { Provider } from 'redux-bundler-preact'
import sorghum from 'sorghum-search'
import gramene from 'gramene-search'

const SorghumList = sorghum.resultList;
const GrameneList = gramene.resultList;
export default (store) => (
  <Provider store={store}>
    <div>
      <SorghumList />
      <GrameneList />
    </div>
  </Provider>
)
