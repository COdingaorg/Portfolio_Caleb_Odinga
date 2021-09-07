import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ListprofileComponent } from './listprofile/listprofile.component';
import { ListbackgroundComponent } from './listbackground/listbackground.component';
import { ListskillsComponent } from './listskills/listskills.component';
import { ListcontactComponent } from './listcontact/listcontact.component';
import { ListtoolsComponent } from './listtools/listtools.component';
import { ListsocialComponent } from './listsocial/listsocial.component';
import { ListprojectsComponent } from './listprojects/listprojects.component';

@NgModule({
  declarations: [
    AppComponent,
    ListprofileComponent,
    ListbackgroundComponent,
    ListskillsComponent,
    ListcontactComponent,
    ListtoolsComponent,
    ListsocialComponent,
    ListprojectsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }