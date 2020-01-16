import React from 'react'
import {Provider, connect} from 'redux-bundler-react'
import {DebounceInput} from 'react-debounce-input'
import { Tabs, Tab } from 'react-bootstrap'
import { suggestions as SorghumSummary } from 'sorghum-search'
import { suggestions as GrameneSummary } from 'gramene-search'

const handleKey = (key, props) => {
  if (key === "Escape") {
    props.doClearSuggestions();
  }
  if (key === "Enter") {
    if (props.suggestionsTab === "sorghumbase") {
      props.doAcceptSorghumSuggestion(`q=${props.suggestionsQuery}`)
    }
  }
};

const SearchBarCmp = props =>
    <DebounceInput
        minLength={0}
        debounceTimeout={300}
        onChange={e => props.doChangeSuggestionsQuery(e.target.value)}
        onKeyUp={e => handleKey(e.key,props)}
        className="form-control"
        value={props.suggestionsQuery || ''}
        placeholder="Search Sorghumbase"
        id="sorghumbase-search-input"
        autoComplete="off"
        spellCheck="false"
    />;

const SearchBar = connect(
  'selectSuggestionsQuery',
  'selectSuggestionsTab',
  'doChangeSuggestionsQuery',
  'doClearSuggestions',
  'doAcceptSorghumSuggestion',
  SearchBarCmp
);

const ResultsCmp = ({suggestionsQuery, suggestionsTab, doChangeSuggestionsTab}) => {
  if (suggestionsQuery) {
    return (
      <div className="search-suggestions">
        <Tabs id="controlled-search-tabs" activeKey={suggestionsTab} onSelect={k => doChangeSuggestionsTab(k)}>
          <Tab eventKey="gramene" title="Genes">
            <GrameneSummary/>
          </Tab>
          <Tab eventKey="sorghumbase" title="Website">
            <SorghumSummary/>
          </Tab>
          <Tab eventKey="germplasm" title="Germplasm" disabled>
            <p>placeholder</p>
          </Tab>
        </Tabs>
      </div>
    );
  }
  return null;
}

const Results = connect(
  'selectSuggestionsQuery',
  'selectSuggestionsTab',
  'doChangeSuggestionsTab',
  ResultsCmp
);

export default (store) => {
    return (
        <Provider store={store}>
          <div>
            <SearchBar/>
            <Results/>
          </div>
        </Provider>
    )
}

