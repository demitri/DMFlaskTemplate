import { h } from 'preact'
import { Provider } from 'redux-bundler-preact'
import sorghum from 'sorghum-search'
import gramene from 'gramene-search'

const SorghumSummary = sorghum.resultSummary;
const GrameneSummary = gramene.resultSummary;

export default (store) => (
  <Provider store={store}>
    <ul className="list-unstyled category">
      <SorghumSummary />
    </ul>
  </Provider>
)
