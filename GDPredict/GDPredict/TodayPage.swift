//
//  TodayPage.swift
//  GDPredict
//
//  Created by vic on 8/2/20.
//  Copyright © 2020 XinyiX. All rights reserved.
//

import SwiftUI

struct TodayView: View {
    var body: some View {
        ScrollView{
            VStack{
                HStack{
                    VStack(alignment: .leading){
                        Text("Wednesday August 02")
                            .foregroundColor(Color.gray)
                        Text("Today")
                        .bold()
                        .font(Font.largeTitle)
                    }
                    Spacer()
                    Button(action: self.loadStockList, label:{
                        Image("data-analytics")
                            .resizable()
                            .frame(width: 70.0, height: 70.0, alignment: .trailing)
                            .scaledToFit()
                    }).accentColor(Color.orange)
                        .padding()
            }
          Divider()
        }
        highlightView().frame(height: 400, alignment:.leading)
            
        }
    }
    func loadStockList() {
        
    }
}

struct highlightView: View{
    var body:some View{
        VStack{
            ZStack{
                Image("health").resizable()
            }
        .cornerRadius(30)
        .padding()
            
        }
    }
}
struct TodayView_Previews: PreviewProvider {
    static var previews: some View {
        TodayView()
    }
}
