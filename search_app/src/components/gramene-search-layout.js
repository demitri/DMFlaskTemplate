import React from 'react'
import { Provider, connect } from 'redux-bundler-react'
import { Status, Filters, Results, Views } from 'gramene-search'
import HelpDemo from './HelpDemo'

const ResultsOrHelpCmp = props => {
  return props.grameneFilters.rightIdx > 1 ? <Results/> : <HelpDemo/>;
}

const ResultsOrHelp = connect(
    'selectGrameneFilters',
    ResultsOrHelpCmp
)

const GrameneSearchLayout = (store) => (
  <Provider store={store}>
    <div className="row no-margin no-padding">
      <div className="col-md-2 no-padding">
        <div className="gramene-sidebar">
          <Status/>
          <Filters/>
          {/*<Views/>*/}
        </div>
      </div>
      <div className="col-md-10 no-padding">
        <ResultsOrHelp/>
      </div>
    </div>
  </Provider>
);

export default GrameneSearchLayout;
