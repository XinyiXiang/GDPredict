//
//  HomePage.swift
//  GDPredict
//
//  Created by vic on 8/2/20.
//  Copyright © 2020 XinyiX. All rights reserved.
//

import SwiftUI

struct HomeView: View {
    @State var selected: Int  = 0
    var body: some View {
        TabView(selection: $selected){ TodayView().tabItem{
                Text("Today")
            }
            PredictionView().tabItem{
                Text("Prediction")
            }
            ResultsView().tabItem{
                Text("Results")
            }
            
        }
    }
}
    
struct HomeView_Previews: PreviewProvider {
    static var previews: some View {
        HomeView()
    }
}
